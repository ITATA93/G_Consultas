# SQLUser.ORC_PlacentaExpulsionComplic

**Schema:** SQLUser
**Columnas:** 23
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Órdenes**. Parámetros de órdenes médicas.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PLEXCO_RowId | bigint | PK |  | NO | - |
| PLEXCO_Code | varchar |  |  | NO | Code |
| PLEXCO_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| PLEXCO_CreatedDate | date |  |  | SI | Created Date |
| PLEXCO_CreatedTime | time |  |  | SI | Created Time |
| PLEXCO_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PLEXCO_DateFrom | date |  |  | SI | Date From |
| PLEXCO_DateTo | date |  |  | SI | Date To |
| PLEXCO_Desc | varchar |  |  | NO | Description |
| PLEXCO_Owner | varchar |  |  | SI | Owner |
| PLEXCO_UpdatedDate | date |  |  | SI | Updated Date |
| PLEXCO_UpdatedTime | time |  |  | SI | Updated Time |
| PLEXCO_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q39Q1 | - |  |  | SI | Attempt |
| Q39Q2 | - |  |  | SI | Intubator |
| Q39Q3 | - |  |  | SI | Intubation experience level |
| Q39Q4 | - |  |  | SI | Laryngoscope |
| Q39Q5 | - |  |  | SI | Cormack and Lehane grade |
| Q39Q6 | - |  |  | SI | External laryngeal manipulation |
| Q39Q7 | - |  |  | SI | Cricoid	 |
| Q39Q8 | - |  |  | SI | Manual in-line stabilisation |
| Q39Q9 | - |  |  | SI | Intubation assisting devices used? |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*