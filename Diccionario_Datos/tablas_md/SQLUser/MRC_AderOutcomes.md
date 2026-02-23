# SQLUser.MRC_AderOutcomes

**Schema:** SQLUser
**Columnas:** 19
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Registros Médicos**. Parámetros de historia clínica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ADERO_RowID | bigint | PK |  | NO | - |
| ADERO_Code | varchar |  |  | SI | Code |
| ADERO_CodeTableTags | varchar |  |  | SI | Code table tags |
| ADERO_CreatedDate | date |  |  | SI | Created Date |
| ADERO_CreatedTime | time |  |  | SI | Created Time |
| ADERO_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ADERO_DateFrom | date |  |  | SI | Date From |
| ADERO_DateTo | date |  |  | SI | Date To |
| ADERO_Desc | varchar |  |  | SI | Description |
| ADERO_Owner | varchar |  |  | SI | Owner |
| ADERO_UpdatedDate | date |  |  | SI | Updated Date |
| ADERO_UpdatedTime | time |  |  | SI | Updated Time |
| ADERO_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| ChildQ93DR | - |  |  | SI | Child Reference: Cardíaco |
| Q89Q1 | - |  |  | SI | Percusión |
| Q89Q2 | - |  |  | SI | Auscultación |
| Q89Q3 | - |  |  | SI | Localización |
| Q89Q4 | - |  |  | SI | Comentario |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*