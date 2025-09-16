import { errorHandler } from '@backstage/backend-common';
import express from 'express';
import Router from 'express-promise-router';
import { Logger } from 'winston';
import { Config } from '@backstage/config';
import { LangfuseClient } from './LangfuseClient';

export interface RouterOptions {
  logger: Logger;
  config: Config;
}

export async function createRouter(
  options: RouterOptions,
): Promise<express.Router> {
  const { logger, config } = options;

  const langfuseConfig = config.getConfig('nova.langfuse');
  const baseUrl = langfuseConfig.getString('baseUrl');
  const publicKey = langfuseConfig.getString('publicKey');
  const secretKey = langfuseConfig.getString('secretKey');

  const langfuseClient = new LangfuseClient({
    baseUrl,
    publicKey,
    secretKey,
    logger,
  });

  const router = Router();
  router.use(express.json());

  // Health check endpoint
  router.get('/health', (_, response) => {
    logger.info('Health check endpoint called');
    response.json({ status: 'ok' });
  });

  // Get all prompts from Langfuse
  router.get('/prompts', async (req, response) => {
    try {
      logger.info('Fetching prompts from Langfuse');
      const { page = 1, limit = 50, search = '' } = req.query;
      
      const prompts = await langfuseClient.getPrompts({
        page: Number(page),
        limit: Number(limit),
        search: String(search),
      });

      response.json({
        success: true,
        data: prompts,
        metadata: {
          page: Number(page),
          limit: Number(limit),
          total: prompts.length,
        },
      });
    } catch (error) {
      logger.error('Error fetching prompts:', error);
      response.status(500).json({
        success: false,
        error: 'Failed to fetch prompts from Langfuse',
      });
    }
  });

  // Get specific prompt by name
  router.get('/prompts/:name', async (req, response) => {
    try {
      const { name } = req.params;
      logger.info(`Fetching prompt: ${name}`);
      
      const prompt = await langfuseClient.getPrompt(name);
      
      if (!prompt) {
        return response.status(404).json({
          success: false,
          error: 'Prompt not found',
        });
      }

      response.json({
        success: true,
        data: prompt,
      });
    } catch (error) {
      logger.error('Error fetching prompt:', error);
      response.status(500).json({
        success: false,
        error: 'Failed to fetch prompt from Langfuse',
      });
    }
  });

  // Get traces (execution history)
  router.get('/traces', async (req, response) => {
    try {
      logger.info('Fetching traces from Langfuse');
      const { page = 1, limit = 50, sessionId, userId } = req.query;
      
      const traces = await langfuseClient.getTraces({
        page: Number(page),
        limit: Number(limit),
        sessionId: sessionId as string,
        userId: userId as string,
      });

      response.json({
        success: true,
        data: traces,
        metadata: {
          page: Number(page),
          limit: Number(limit),
        },
      });
    } catch (error) {
      logger.error('Error fetching traces:', error);
      response.status(500).json({
        success: false,
        error: 'Failed to fetch traces from Langfuse',
      });
    }
  });

  // Get scores/evaluations
  router.get('/scores', async (req, response) => {
    try {
      logger.info('Fetching scores from Langfuse');
      const { traceId } = req.query;
      
      if (!traceId) {
        return response.status(400).json({
          success: false,
          error: 'traceId is required',
        });
      }

      const scores = await langfuseClient.getScores(String(traceId));

      response.json({
        success: true,
        data: scores,
      });
    } catch (error) {
      logger.error('Error fetching scores:', error);
      response.status(500).json({
        success: false,
        error: 'Failed to fetch scores from Langfuse',
      });
    }
  });

  // Get sessions
  router.get('/sessions', async (req, response) => {
    try {
      logger.info('Fetching sessions from Langfuse');
      const { page = 1, limit = 50 } = req.query;
      
      const sessions = await langfuseClient.getSessions({
        page: Number(page),
        limit: Number(limit),
      });

      response.json({
        success: true,
        data: sessions,
        metadata: {
          page: Number(page),
          limit: Number(limit),
        },
      });
    } catch (error) {
      logger.error('Error fetching sessions:', error);
      response.status(500).json({
        success: false,
        error: 'Failed to fetch sessions from Langfuse',
      });
    }
  });

  // Get metrics/statistics
  router.get('/metrics', async (req, response) => {
    try {
      logger.info('Fetching metrics from Langfuse');
      const { startDate, endDate } = req.query;
      
      const metrics = await langfuseClient.getMetrics({
        startDate: startDate as string,
        endDate: endDate as string,
      });

      response.json({
        success: true,
        data: metrics,
      });
    } catch (error) {
      logger.error('Error fetching metrics:', error);
      response.status(500).json({
        success: false,
        error: 'Failed to fetch metrics from Langfuse',
      });
    }
  });

  // Search across all entities
  router.post('/search', async (req, response) => {
    try {
      const { query, filters = {}, limit = 50 } = req.body;
      logger.info(`Searching Langfuse with query: ${query}`);
      
      const results = await langfuseClient.search({
        query,
        filters,
        limit,
      });

      response.json({
        success: true,
        data: results,
      });
    } catch (error) {
      logger.error('Error searching:', error);
      response.status(500).json({
        success: false,
        error: 'Failed to search Langfuse',
      });
    }
  });

  router.use(errorHandler());
  return router;
}