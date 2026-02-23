# SQLUser.ARC_InsurAssociation

**Schema:** SQLUser
**Columnas:** 34
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Seguros**. Planes y convenios.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| INSAS_RowId | bigint | PK |  | NO | - |
| ChildQ85DR | - |  |  | SI | Child Reference: Introspección y Juicio |
| INSAS_Address | varchar |  |  | SI | Address |
| INSAS_BillingAddress | varchar |  |  | SI | Billing Address |
| INSAS_City_DR | bigint |  | FK | SI | Des Ref City |
| INSAS_Code | varchar |  |  | NO | Code |
| INSAS_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| INSAS_CodeTranslated | varchar |  |  | SI | - |
| INSAS_CreatedDate | date |  |  | SI | Created Date |
| INSAS_CreatedTime | time |  |  | SI | Created Time |
| INSAS_CreatedUser_DR | bigint |  | FK | SI | Created User |
| INSAS_DateTo | date |  |  | SI | Date To |
| INSAS_Desc | varchar |  |  | NO | Insur Assoc Name |
| INSAS_DescTranslated | varchar |  |  | SI | - |
| INSAS_Email | varchar |  |  | SI | Email |
| INSAS_Fax | varchar |  |  | SI | Fax |
| INSAS_GovernmentNumber | varchar |  |  | SI | Government Number |
| INSAS_InsType_DR | bigint |  | FK | NO | Des Ref to InsType |
| INSAS_InvoiceWay | varchar |  |  | SI | Invoice Way |
| INSAS_Notes | varchar |  |  | SI | Notes |
| INSAS_OfficeAgent_DR | bigint |  | FK | SI | Des Ref OfficeAgent |
| INSAS_OfficeCateg_DR | bigint |  | FK | SI | Des Ref OfficeCateg |
| INSAS_OfficePaymCondit_DR | bigint |  | FK | SI | Des Ref OfficePaymCondition |
| INSAS_Owner | varchar |  |  | SI | Owner |
| INSAS_Phone | varchar |  |  | SI | Phone |
| INSAS_StartDate | date |  |  | SI | Start Date of Service |
| INSAS_StateNumber | varchar |  |  | SI | State Number |
| INSAS_UpdatedDate | date |  |  | SI | Updated Date |
| INSAS_UpdatedTime | time |  |  | SI | Updated Time |
| INSAS_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| INSAS_Zip_DR | bigint |  | FK | SI | Des Ref to CTZip |
| Q253Q1 | - |  |  | SI | Evaluación |
| Q253Q2 | - |  |  | SI | Comentarios (Texto libre) |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*