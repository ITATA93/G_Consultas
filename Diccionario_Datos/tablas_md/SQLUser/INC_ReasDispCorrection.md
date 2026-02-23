# SQLUser.INC_ReasDispCorrection

**Schema:** SQLUser
**Columnas:** 22
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Incidentes**. Reportes de eventos adversos.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| INRDC_RowId | bigint | PK |  | NO | - |
| INRDC_Code | varchar |  |  | NO | Code |
| INRDC_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| INRDC_CreatedDate | date |  |  | SI | Created Date |
| INRDC_CreatedTime | time |  |  | SI | Created Time |
| INRDC_CreatedUser_DR | bigint |  | FK | SI | Created User |
| INRDC_DateFrom | date |  |  | SI | Date From |
| INRDC_DateTo | date |  |  | SI | Date To |
| INRDC_Desc | varchar |  |  | NO | Description |
| INRDC_Owner | varchar |  |  | SI | Owner |
| INRDC_UpdatedDate | date |  |  | SI | Updated Date |
| INRDC_UpdatedTime | time |  |  | SI | Updated Time |
| INRDC_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q27Q1 | - |  |  | SI | Date |
| Q27Q2 | - |  |  | SI | Time |
| Q27Q3 | - |  |  | SI | Drain name |
| Q27Q4 | - |  |  | SI | Insertion site check |
| Q27Q5 | - |  |  | SI | Dressing status |
| Q27Q6 | - |  |  | SI | Actions performed |
| Q27Q7 | - |  |  | SI | Assessment notes |
| Q27Q8 | - |  |  | SI | Assessment performed by |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*