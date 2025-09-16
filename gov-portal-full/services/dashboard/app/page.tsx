'use client'

import { Card, Grid, Title, Text, Tab, TabList, TabGroup, TabPanel, TabPanels, Metric, ProgressBar, BadgeDelta, Flex, AreaChart, DonutChart, BarList, Table, TableHead, TableRow, TableHeaderCell, TableBody, TableCell, Badge } from '@tremor/react'
import { ArrowUpIcon, ArrowDownIcon, UserGroupIcon, AcademicCapIcon, ChartBarIcon, ClockIcon } from '@heroicons/react/24/solid'
import { useState, useEffect } from 'react'

// Mock data - In production, this would come from API/Supabase
const impactMetrics = {
  implementation: { value: 75, delta: 12, deltaType: 'increase' as const },
  momentum: { value: 68, delta: -3, deltaType: 'decrease' as const },
  performance: { value: 82, delta: 8, deltaType: 'increase' as const },
  acceptance: { value: 71, delta: 5, deltaType: 'increase' as const },
  costEffective: { value: 89, delta: 15, deltaType: 'increase' as const },
  trust: { value: 77, delta: 2, deltaType: 'increase' as const },
}

const adoptionData = [
  { month: 'Ene', 'Nova-Cell': 45, 'GitHub Copilot': 32, 'Claude': 28, 'OpenAI': 38 },
  { month: 'Feb', 'Nova-Cell': 52, 'GitHub Copilot': 38, 'Claude': 35, 'OpenAI': 42 },
  { month: 'Mar', 'Nova-Cell': 61, 'GitHub Copilot': 45, 'Claude': 42, 'OpenAI': 48 },
  { month: 'Abr', 'Nova-Cell': 68, 'GitHub Copilot': 52, 'Claude': 48, 'OpenAI': 55 },
  { month: 'May', 'Nova-Cell': 75, 'GitHub Copilot': 58, 'Claude': 55, 'OpenAI': 61 },
]

const trainingMetrics = {
  totalEnrolled: 487,
  activeUsers: 312,
  completionRate: 73,
  avgTimeToComplete: 14.5,
  trackDistribution: [
    { name: 'Fundacional', value: 145 },
    { name: 'Analysts', value: 89 },
    { name: 'Developers', value: 78 },
    { name: 'Marketing', value: 67 },
    { name: 'Compliance', value: 45 },
  ],
}

const topCourses = [
  { name: 'Fundamentos GenAI', enrollments: 145, completion: 78 },
  { name: 'Prompt Engineering', enrollments: 112, completion: 65 },
  { name: 'APIs de IA', enrollments: 98, completion: 71 },
  { name: 'ISO 42001', enrollments: 76, completion: 82 },
  { name: 'Ética en IA', enrollments: 65, completion: 88 },
]

const squadsData = [
  { squad: 'Riesgos', status: 'Federado', po: 'María García', ro: 'Juan Pérez', adoption: 85 },
  { squad: 'Digital Banking', status: 'Federado', po: 'Carlos López', ro: 'Ana Martínez', adoption: 78 },
  { squad: 'Infraestructura', status: 'Shadow', po: '-', ro: 'Pedro Sánchez', adoption: 45 },
  { squad: 'Marketing', status: 'Federado', po: 'Laura Torres', ro: 'Diego Ruiz', adoption: 92 },
  { squad: 'Compliance', status: 'Shadow', po: '-', ro: 'Sofia Mendez', adoption: 38 },
]

export default function Dashboard() {
  const [selectedTab, setSelectedTab] = useState(0)
  const [currentTime, setCurrentTime] = useState(new Date())

  useEffect(() => {
    const timer = setInterval(() => setCurrentTime(new Date()), 1000)
    return () => clearInterval(timer)
  }, [])

  return (
    <main className="p-4 md:p-10 mx-auto max-w-7xl">
      <Flex className="mb-4">
        <div>
          <Title>Portal de Gobernanza de IA - Tablero</Title>
          <Text>Centro de Excelencia de IA - Métricas IMPACT y Adopción</Text>
        </div>
        <Badge color="blue">{currentTime.toLocaleString('es-MX')}</Badge>
      </Flex>

      <TabGroup index={selectedTab} onIndexChange={setSelectedTab}>
        <TabList className="mt-8">
          <Tab icon={ChartBarIcon}>Métricas IMPACT</Tab>
          <Tab icon={UserGroupIcon}>Adopción</Tab>
          <Tab icon={AcademicCapIcon}>Capacitación</Tab>
          <Tab icon={ClockIcon}>Squads</Tab>
        </TabList>
        <TabPanels>
          {/* IMPACT Metrics Panel */}
          <TabPanel>
            <Grid numItemsMd={2} numItemsLg={3} className="gap-6 mt-6">
              <Card>
                <Text>Implementación</Text>
                <Metric>{impactMetrics.implementation.value}%</Metric>
                <Flex className="mt-4">
                  <Text className="truncate">vs último mes</Text>
                  <BadgeDelta deltaType={impactMetrics.implementation.deltaType}>
                    {impactMetrics.implementation.delta}%
                  </BadgeDelta>
                </Flex>
                <ProgressBar value={impactMetrics.implementation.value} className="mt-2" />
              </Card>

              <Card>
                <Text>Impulso</Text>
                <Metric>{impactMetrics.momentum.value}%</Metric>
                <Flex className="mt-4">
                  <Text className="truncate">vs último mes</Text>
                  <BadgeDelta deltaType={impactMetrics.momentum.deltaType}>
                    {impactMetrics.momentum.delta}%
                  </BadgeDelta>
                </Flex>
                <ProgressBar value={impactMetrics.momentum.value} className="mt-2" />
              </Card>

              <Card>
                <Text>Desempeño</Text>
                <Metric>{impactMetrics.performance.value}%</Metric>
                <Flex className="mt-4">
                  <Text className="truncate">vs último mes</Text>
                  <BadgeDelta deltaType={impactMetrics.performance.deltaType}>
                    {impactMetrics.performance.delta}%
                  </BadgeDelta>
                </Flex>
                <ProgressBar value={impactMetrics.performance.value} className="mt-2" />
              </Card>

              <Card>
                <Text>Aceptación</Text>
                <Metric>{impactMetrics.acceptance.value}%</Metric>
                <Flex className="mt-4">
                  <Text className="truncate">vs último mes</Text>
                  <BadgeDelta deltaType={impactMetrics.acceptance.deltaType}>
                    {impactMetrics.acceptance.delta}%
                  </BadgeDelta>
                </Flex>
                <ProgressBar value={impactMetrics.acceptance.value} className="mt-2" />
              </Card>

              <Card>
                <Text>Costo-Efectividad</Text>
                <Metric>{impactMetrics.costEffective.value}%</Metric>
                <Flex className="mt-4">
                  <Text className="truncate">vs último mes</Text>
                  <BadgeDelta deltaType={impactMetrics.costEffective.deltaType}>
                    {impactMetrics.costEffective.delta}%
                  </BadgeDelta>
                </Flex>
                <ProgressBar value={impactMetrics.costEffective.value} className="mt-2" />
              </Card>

              <Card>
                <Text>Confianza</Text>
                <Metric>{impactMetrics.trust.value}%</Metric>
                <Flex className="mt-4">
                  <Text className="truncate">vs último mes</Text>
                  <BadgeDelta deltaType={impactMetrics.trust.deltaType}>
                    {impactMetrics.trust.delta}%
                  </BadgeDelta>
                </Flex>
                <ProgressBar value={impactMetrics.trust.value} className="mt-2" />
              </Card>
            </Grid>

            <Card className="mt-6">
              <Title>Tendencia Global IMPACT</Title>
              <AreaChart
                className="h-72 mt-4"
                data={adoptionData}
                index="month"
                categories={['Nova-Cell', 'GitHub Copilot', 'Claude', 'OpenAI']}
                colors={['indigo', 'cyan', 'amber', 'emerald']}
                valueFormatter={(value) => `${value}%`}
              />
            </Card>
          </TabPanel>

          {/* Adopción Panel */}
          <TabPanel>
            <Grid numItemsMd={2} className="gap-6 mt-6">
              <Card>
                <Title>Adopción por Proveedor de IA</Title>
                <DonutChart
                  className="mt-6"
                  data={[
                    { name: 'Nova-Cell', value: 75 },
                    { name: 'GitHub Copilot', value: 58 },
                    { name: 'Claude', value: 55 },
                    { name: 'OpenAI', value: 61 },
                    { name: 'Gemini', value: 42 },
                  ]}
                  category="value"
                  index="name"
                  valueFormatter={(value) => `${value}%`}
                  colors={['slate', 'violet', 'indigo', 'rose', 'cyan']}
                />
              </Card>

              <Card>
                <Title>Tendencia de Adopción</Title>
                <AreaChart
                  className="h-72 mt-4"
                  data={adoptionData}
                  index="month"
                  categories={['Nova-Cell', 'GitHub Copilot', 'Claude', 'OpenAI']}
                  colors={['indigo', 'cyan', 'amber', 'emerald']}
                  valueFormatter={(value) => `${value}%`}
                />
              </Card>
            </Grid>

            <Card className="mt-6">
              <Title>Métricas de Adopción Detalladas</Title>
              <Grid numItemsMd={4} className="gap-4 mt-4">
                <Card decoration="top" decorationColor="indigo">
                  <Text>Usuarios Activos</Text>
                  <Metric>1,248</Metric>
                </Card>
                <Card decoration="top" decorationColor="cyan">
                  <Text>Tiempo al Primer Valor (min)</Text>
                  <Metric>12.3</Metric>
                </Card>
                <Card decoration="top" decorationColor="amber">
                  <Text>Puntuación NPS</Text>
                  <Metric>42</Metric>
                </Card>
                <Card decoration="top" decorationColor="emerald">
                  <Text>ROI</Text>
                  <Metric>3.2x</Metric>
                </Card>
              </Grid>
            </Card>
          </TabPanel>

          {/* Training Panel */}
          <TabPanel>
            <Grid numItemsMd={2} numItemsLg={4} className="gap-6 mt-6">
              <Card>
                <Text>Total Inscritos</Text>
                <Metric>{trainingMetrics.totalEnrolled}</Metric>
                <Text className="mt-2">usuarios</Text>
              </Card>
              <Card>
                <Text>Usuarios Activos</Text>
                <Metric>{trainingMetrics.activeUsers}</Metric>
                <Text className="mt-2">esta semana</Text>
              </Card>
              <Card>
                <Text>Tasa de Finalización</Text>
                <Metric>{trainingMetrics.completionRate}%</Metric>
                <ProgressBar value={trainingMetrics.completionRate} className="mt-2" />
              </Card>
              <Card>
                <Text>Tiempo Promedio</Text>
                <Metric>{trainingMetrics.avgTimeToComplete}</Metric>
                <Text className="mt-2">días</Text>
              </Card>
            </Grid>

            <Grid numItemsMd={2} className="gap-6 mt-6">
              <Card>
                <Title>Distribución por Ruta de Aprendizaje</Title>
                <DonutChart
                  className="mt-6"
                  data={trainingMetrics.trackDistribution}
                  category="value"
                  index="name"
                  colors={['slate', 'violet', 'indigo', 'rose', 'cyan']}
                />
              </Card>

              <Card>
                <Title>Cursos Principales</Title>
                <BarList
                  className="mt-4"
                  data={topCourses.map(course => ({
                    name: course.name,
                    value: course.enrollments,
                    completion: course.completion,
                  }))}
                  valueFormatter={(value: number) => `${value} inscritos`}
                />
              </Card>
            </Grid>
          </TabPanel>

          {/* Squads Panel */}
          <TabPanel>
            <Card className="mt-6">
              <Title>Estado de Squads - Modelo Federado</Title>
              <Table className="mt-4">
                <TableHead>
                  <TableRow>
                    <TableHeaderCell>Squad</TableHeaderCell>
                    <TableHeaderCell>Estado</TableHeaderCell>
                    <TableHeaderCell>Dueño del Producto</TableHeaderCell>
                    <TableHeaderCell>Oficial de Riesgos</TableHeaderCell>
                    <TableHeaderCell>Adopción</TableHeaderCell>
                  </TableRow>
                </TableHead>
                <TableBody>
                  {squadsData.map((squad) => (
                    <TableRow key={squad.squad}>
                      <TableCell>{squad.squad}</TableCell>
                      <TableCell>
                        <Badge color={squad.status === 'Federado' ? 'emerald' : 'amber'}>
                          {squad.status}
                        </Badge>
                      </TableCell>
                      <TableCell>{squad.po}</TableCell>
                      <TableCell>{squad.ro}</TableCell>
                      <TableCell>
                        <Flex>
                          <Text>{squad.adoption}%</Text>
                          <ProgressBar value={squad.adoption} className="ml-2" />
                        </Flex>
                      </TableCell>
                    </TableRow>
                  ))}
                </TableBody>
              </Table>
            </Card>

            <Grid numItemsMd={3} className="gap-6 mt-6">
              <Card>
                <Text>Squads Federados</Text>
                <Metric>3/5</Metric>
                <ProgressBar value={60} className="mt-2" />
              </Card>
              <Card>
                <Text>Cobertura PO/RO</Text>
                <Metric>80%</Metric>
                <Text className="mt-2">4 de 5 squads con roles</Text>
              </Card>
              <Card>
                <Text>Madurez Promedio</Text>
                <Metric>67%</Metric>
                <BadgeDelta deltaType="increase" className="mt-2">
                  +12% este mes
                </BadgeDelta>
              </Card>
            </Grid>
          </TabPanel>
        </TabPanels>
      </TabGroup>
    </main>
  )
}