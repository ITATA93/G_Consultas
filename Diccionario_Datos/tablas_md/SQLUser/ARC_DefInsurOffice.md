# SQLUser.ARC_DefInsurOffice

**Schema:** SQLUser
**Columnas:** 20
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Arquetipo de configuración**. Definición base del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DEFINS_RowId | bigint | PK |  | NO | - |
| ChildQ45DR | - |  |  | SI | Child Reference: Extremidades |
| DEFINS_AuxInsType_DR | bigint |  | FK | SI | Des Ref AuxInsType |
| DEFINS_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| DEFINS_CreatedDate | date |  |  | SI | Created Date |
| DEFINS_CreatedTime | time |  |  | SI | Created Time |
| DEFINS_CreatedUser_DR | bigint |  | FK | SI | Created User |
| DEFINS_Hospital_DR | bigint |  | FK | SI | Des Ref Hospital |
| DEFINS_InsAssoc_DR | bigint |  | FK | SI | Des Ref InsAssoc |
| DEFINS_InsType_DR | bigint |  | FK | SI | Des Ref InsType |
| DEFINS_Owner | varchar |  |  | SI | Owner |
| DEFINS_UpdatedDate | date |  |  | SI | Updated Date |
| DEFINS_UpdatedTime | time |  |  | SI | Updated Time |
| DEFINS_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q39Q1 | - |  |  | SI | Palpación |
| Q39Q2 | - |  |  | SI | Percusión |
| Q39Q3 | - |  |  | SI | Auscultación |
| Q39Q4 | - |  |  | SI | Localización |
| Q39Q5 | - |  |  | SI | Comentario |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*