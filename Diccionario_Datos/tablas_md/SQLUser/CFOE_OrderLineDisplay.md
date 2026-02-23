# SQLUser.CFOE_OrderLineDisplay

**Schema:** SQLUser
**Columnas:** 19
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Órdenes Médicas**. Solicitudes de exámenes, procedimientos, etc.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ORDLINEDIS_RowId | bigint | PK |  | NO | - |
| ChildQ02DR | - |  |  | SI | Child Reference: METAS |
| ORDLINEDIS_CondensedStyle | varchar |  |  | SI | Use the CONDENSED style for OrderLine  |
| ORDLINEDIS_EpisType | varchar |  |  | NO | EpisType |
| ORDLINEDIS_ExpandDMCycleDetails | varchar |  |  | SI | Expand details if Dosing Model Cycle used for orde... |
| ORDLINEDIS_ShowDuration | varchar |  |  | SI | Default |
| ORDLINEDIS_ShowGenericBrand | varchar |  |  | SI | Show Generic/Brand |
| ORDLINEDIS_ShowLastDose | varchar |  |  | SI | Show Last Dose |
| ORDLINEDIS_ShowOrderEndDate | varchar |  |  | SI | Show Order End Date |
| ORDLINEDIS_ShowPackSize | varchar |  |  | SI | Pack Size |
| ORDLINEDIS_ShowRateIVCont | varchar |  |  | SI | Show Rate IV Continuous |
| Q04Q1 | - |  |  | SI | Objetivos |
| Q04Q2 | - |  |  | SI | Estrategias o Actividades |
| Q04Q3 | - |  |  | SI | Responsables |
| Q04Q4 | - |  |  | SI | Plazo |
| Q04Q5 | - |  |  | SI | Resultados |
| Q04Q6 | - |  |  | SI | Logros |
| Q04Q7 | - |  |  | SI | Comentarios |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*