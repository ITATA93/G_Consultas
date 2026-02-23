# SQLUser.MRC_WordResultCodeUsers

**Schema:** SQLUser
**Columnas:** 20
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Registros Médicos**. Parámetros de historia clínica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| USR_ParRef | bigint | PK |  | NO | MRC_WordResultCode Parent Reference |
| ChildQ04DR | - |  |  | SI | Child Reference: Cuidador 6 Horas |
| Q03Q10 | - |  |  | SI | Servicio Clínico |
| Q03Q11 | - |  |  | SI | Recibió Alimentación Asistida |
| Q03Q5 | - |  |  | SI | Turno Mañana 08:00 a 14:00 |
| Q03Q6 | - |  |  | SI | Turno Tarde 14:00 a 20:00 |
| Q03Q7 | - |  |  | SI | Turno Noche 20:00 a 08:00 |
| Q03Q8 | - |  |  | SI | Nombre del Cuidador |
| Q03Q9 | - |  |  | SI | Fecha |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| USR_Childsub | double |  |  | NO | Childsub |
| USR_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| USR_CreatedDate | date |  |  | SI | Created Date |
| USR_CreatedTime | time |  |  | SI | Created Time |
| USR_CreatedUser_DR | bigint |  | FK | SI | Created User |
| USR_RowId | varchar |  |  | NO | - |
| USR_UpdatedDate | date |  |  | SI | Updated Date |
| USR_UpdatedTime | time |  |  | SI | Updated Time |
| USR_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| USR_User_DR | bigint |  | FK | SI | Des Ref User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*