# SQLUser.LBC_StorageScheme

**Schema:** SQLUser
**Columnas:** 29
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Laboratorio**. Parámetros del módulo de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCSS_RowID | bigint | PK |  | NO | - |
| LBCSS_Code | varchar |  |  | NO | Code |
| LBCSS_CodeTableTags | varchar |  |  | SI | List of code table tags |
| LBCSS_CreatedDate | date |  |  | SI | Created Date |
| LBCSS_CreatedTime | time |  |  | SI | Created Time |
| LBCSS_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LBCSS_DateFrom | date |  |  | SI | Effective date for the record |
| LBCSS_DateTo | date |  |  | SI | Last day the record is active |
| LBCSS_Desc | varchar |  |  | NO | Description |
| LBCSS_LongTerm | varchar |  |  | SI | Long Term |
| LBCSS_Owner | varchar |  |  | SI | Owner |
| LBCSS_StartPosition | varchar |  |  | SI | Start Position
This is used on Lab Storage Contai... |
| LBCSS_StorageTime | numeric |  |  | SI | Storage Time |
| LBCSS_StorageTimeCalc | varchar |  |  | SI | Storage Time Calculation
LBCStorageContainerTimeC... |
| LBCSS_StorageTimeUnit | varchar |  |  | SI | Storage Time Unit |
| LBCSS_Storage_DR | bigint |  | FK | SI | Storage Location |
| LBCSS_UpdatedDate | date |  |  | SI | Updated Date |
| LBCSS_UpdatedTime | time |  |  | SI | Updated Time |
| LBCSS_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q08Q10 | - |  |  | SI | Estado Paciente |
| Q08Q11 | - |  |  | SI | Control Medico |
| Q08Q12 | - |  |  | SI | Hora Retiro Sujeciones |
| Q08Q14 | - |  |  | SI | Profesional |
| Q08Q15 | - |  |  | SI | Revisión |
| Q08Q16 | - |  |  | SI | Prevención de Eventos Adversos |
| Q08Q7 | - |  |  | SI | Horario Inicio |
| Q08Q8 | - |  |  | SI | Tipo de Contención |
| Q08Q9 | - |  |  | SI | Estado Contención |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*