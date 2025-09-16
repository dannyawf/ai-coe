import axios, { AxiosInstance } from 'axios';
import { Logger } from 'winston';

export interface LangfuseClientConfig {
  baseUrl: string;
  publicKey: string;
  secretKey: string;
  logger: Logger;
}

export interface PromptQuery {
  page?: number;
  limit?: number;
  search?: string;
}

export interface TraceQuery {
  page?: number;
  limit?: number;
  sessionId?: string;
  userId?: string;
}

export interface SessionQuery {
  page?: number;
  limit?: number;
}

export interface MetricsQuery {
  startDate?: string;
  endDate?: string;
}

export interface SearchQuery {
  query: string;
  filters?: Record<string, any>;
  limit?: number;
}

export class LangfuseClient {
  private client: AxiosInstance;
  private logger: Logger;

  constructor(config: LangfuseClientConfig) {
    const { baseUrl, publicKey, secretKey, logger } = config;
    this.logger = logger;

    // Create axios instance with auth headers
    this.client = axios.create({
      baseURL: baseUrl,
      headers: {
        'X-API-KEY': publicKey,
        'Authorization': `Bearer ${secretKey}`,
        'Content-Type': 'application/json',
      },
      timeout: 30000,
    });

    // Request interceptor for logging
    this.client.interceptors.request.use(
      (config) => {
        this.logger.debug(`Langfuse API Request: ${config.method?.toUpperCase()} ${config.url}`);
        return config;
      },
      (error) => {
        this.logger.error('Langfuse API Request Error:', error);
        return Promise.reject(error);
      }
    );

    // Response interceptor for error handling
    this.client.interceptors.response.use(
      (response) => {
        this.logger.debug(`Langfuse API Response: ${response.status}`);
        return response;
      },
      (error) => {
        this.logger.error('Langfuse API Response Error:', error.response?.data || error.message);
        return Promise.reject(error);
      }
    );
  }

  async getPrompts(query: PromptQuery = {}) {
    try {
      const { page = 1, limit = 50, search = '' } = query;
      const response = await this.client.get('/api/public/prompts', {
        params: {
          page,
          limit,
          search,
        },
      });
      return response.data;
    } catch (error) {
      this.logger.error('Failed to fetch prompts:', error);
      throw error;
    }
  }

  async getPrompt(name: string) {
    try {
      const response = await this.client.get(`/api/public/prompts/${encodeURIComponent(name)}`);
      return response.data;
    } catch (error) {
      this.logger.error(`Failed to fetch prompt ${name}:`, error);
      throw error;
    }
  }

  async getTraces(query: TraceQuery = {}) {
    try {
      const { page = 1, limit = 50, sessionId, userId } = query;
      const params: any = { page, limit };
      
      if (sessionId) params.sessionId = sessionId;
      if (userId) params.userId = userId;

      const response = await this.client.get('/api/public/traces', { params });
      return response.data;
    } catch (error) {
      this.logger.error('Failed to fetch traces:', error);
      throw error;
    }
  }

  async getScores(traceId: string) {
    try {
      const response = await this.client.get(`/api/public/scores`, {
        params: { traceId },
      });
      return response.data;
    } catch (error) {
      this.logger.error(`Failed to fetch scores for trace ${traceId}:`, error);
      throw error;
    }
  }

  async getSessions(query: SessionQuery = {}) {
    try {
      const { page = 1, limit = 50 } = query;
      const response = await this.client.get('/api/public/sessions', {
        params: { page, limit },
      });
      return response.data;
    } catch (error) {
      this.logger.error('Failed to fetch sessions:', error);
      throw error;
    }
  }

  async getMetrics(query: MetricsQuery = {}) {
    try {
      const params: any = {};
      if (query.startDate) params.startDate = query.startDate;
      if (query.endDate) params.endDate = query.endDate;

      const response = await this.client.get('/api/public/metrics', { params });
      return response.data;
    } catch (error) {
      this.logger.error('Failed to fetch metrics:', error);
      throw error;
    }
  }

  async search(query: SearchQuery) {
    try {
      const response = await this.client.post('/api/public/search', {
        query: query.query,
        filters: query.filters || {},
        limit: query.limit || 50,
      });
      return response.data;
    } catch (error) {
      this.logger.error('Failed to search:', error);
      throw error;
    }
  }

  // Additional methods for Nova Cell specific operations

  async getPromptVersions(promptName: string) {
    try {
      const response = await this.client.get(`/api/public/prompts/${encodeURIComponent(promptName)}/versions`);
      return response.data;
    } catch (error) {
      this.logger.error(`Failed to fetch versions for prompt ${promptName}:`, error);
      throw error;
    }
  }

  async getPromptMetadata(promptName: string) {
    try {
      const response = await this.client.get(`/api/public/prompts/${encodeURIComponent(promptName)}/metadata`);
      return response.data;
    } catch (error) {
      this.logger.error(`Failed to fetch metadata for prompt ${promptName}:`, error);
      throw error;
    }
  }

  async getDatasets() {
    try {
      const response = await this.client.get('/api/public/datasets');
      return response.data;
    } catch (error) {
      this.logger.error('Failed to fetch datasets:', error);
      throw error;
    }
  }

  async getDataset(name: string) {
    try {
      const response = await this.client.get(`/api/public/datasets/${encodeURIComponent(name)}`);
      return response.data;
    } catch (error) {
      this.logger.error(`Failed to fetch dataset ${name}:`, error);
      throw error;
    }
  }
}