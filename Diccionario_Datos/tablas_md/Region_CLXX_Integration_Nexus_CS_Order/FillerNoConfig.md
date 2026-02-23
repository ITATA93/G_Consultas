# Region_CLXX_Integration_Nexus_CS_Order.FillerNoConfig

**Schema:** Region_CLXX_Integration_Nexus_CS_Order
**Columnas:** 10
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Configuración del módulo.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| AdmType | varchar |  |  | NO | - |
| Description | varchar |  |  | SI | Description de configuracion |
| MustHaveAppointment | bit |  |  | NO | - |
| OrderItemPriorityCode | varchar |  |  | NO | - |
| OrderItemTimeFrom | time |  |  | SI | - |
| OrderItemTimeTo | time |  |  | SI | - |
| ReceivingLocation | bigint |  |  | NO | Local de Procesamiento |
| SequenceCurrentFillerNo | varchar |  |  | SI | Secuencial actual del día del FillerNo |
| StrategyClassName | varchar |  |  | NO | Nombre de la estrategia o configuracion |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*