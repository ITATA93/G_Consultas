# Region_CLXX_Integration_Nexus_CS_RNI.DocumentRNI

**Schema:** Region_CLXX_Integration_Nexus_CS_RNI
**Columnas:** 16
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Integración Nexus**. Conexión con sistema externo Nexus.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| CreateDate | date |  |  | SI | - |
| CreateTime | time |  |  | SI | - |
| CriterioElegibilidad | bigint |  |  | SI | - |
| Cuestionario | integer |  |  | SI | - |
| CuestionarioId | varchar |  |  | SI | - |
| Dosis | bigint |  |  | SI | - |
| ExternalId | varchar |  |  | SI | - |
| FechaInmunizacion | date |  |  | SI | - |
| Lote | bigint |  |  | SI | - |
| OrderItem | varchar |  |  | SI | - |
| RunPaciente | varchar |  |  | SI | - |
| StatusElimacionRNI | varchar |  |  | SI | - |
| StatusInformacionRNI | varchar |  |  | SI | - |
| StatusRAdversaRNI | varchar |  |  | SI | - |
| Vaccine | bigint |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*