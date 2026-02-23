# SQLUser.MRC_WordResultCode

**Schema:** SQLUser
**Columnas:** 22
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Registros Médicos**. Parámetros de historia clínica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| WORD_RowId | bigint | PK |  | NO | - |
| ChildQ03DR | - |  |  | SI | Child Reference: Cuidador 12 Horas |
| Q02Q1 | - |  |  | SI | Turno Mañana 08:00 a 14:00 |
| Q02Q2 | - |  |  | SI | Turno Tarde 14:00 a 20:00 |
| Q02Q3 | - |  |  | SI | Turno Noche 20:00 a 08:00 |
| Q02Q4 | - |  |  | SI | Nombre del Cuidador |
| Q02Q5 | - |  |  | SI | Fecha |
| Q02Q6 | - |  |  | SI | Servicio Clínico |
| Q02Q7 | - |  |  | SI | Recibió Alimentación Asistida |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| WORD_Code | varchar |  |  | NO | Code |
| WORD_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| WORD_CreatedDate | date |  |  | SI | Created Date |
| WORD_CreatedTime | time |  |  | SI | Created Time |
| WORD_CreatedUser_DR | bigint |  | FK | SI | Created User |
| WORD_OrderSubCat_DR | bigint |  | FK | SI | Des Ref Order Sub Cat |
| WORD_Owner | varchar |  |  | SI | Owner |
| WORD_Text | varchar |  |  | SI | Text |
| WORD_UpdatedDate | date |  |  | SI | Updated Date |
| WORD_UpdatedTime | time |  |  | SI | Updated Time |
| WORD_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| WORD_UserDr | bigint |  |  | SI | des ref to SS_User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*