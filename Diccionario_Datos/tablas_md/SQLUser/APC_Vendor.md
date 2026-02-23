# SQLUser.APC_Vendor

**Schema:** SQLUser
**Columnas:** 56
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Cuentas por Pagar (AP)**. Gestión de proveedores y compras.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| APCVM_RowId | bigint | PK |  | NO | - |
| APCVM_AcctCode_DR | bigint |  | FK | SI | Des Ref to GLCAC |
| APCVM_Addr | varchar |  |  | SI | Address |
| APCVM_Category_DR | bigint |  | FK | SI | Des Ref to APCVC |
| APCVM_City_DR | bigint |  | FK | SI | Des Ref to CTCIT |
| APCVM_CoCode_DR | bigint |  | FK | SI | Des Ref to CTCO |
| APCVM_Code | varchar |  |  | SI | Vendor Code |
| APCVM_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| APCVM_ContPerson | varchar |  |  | SI | Contact Person |
| APCVM_CostCent_DR | bigint |  | FK | SI | Des Ref to GLCCC |
| APCVM_CrAvail | double |  |  | SI | Credit Available |
| APCVM_CrLimit | double |  |  | SI | Credit Limit |
| APCVM_CrTerm | double |  |  | SI | Credit Terms |
| APCVM_CreatedDate | date |  |  | SI | Created Date |
| APCVM_CreatedTime | time |  |  | SI | Created Time |
| APCVM_CreatedUser_DR | bigint |  | FK | SI | Created User |
| APCVM_CreditTerm_DR | bigint |  | FK | SI | Des Ref CreditTerm |
| APCVM_CtrlAcct_DR | varchar |  | FK | SI | Des Ref to APCCA(not in use) -noalert |
| APCVM_CurBal | double |  |  | SI | Current Month Balance |
| APCVM_DateFrom | date |  |  | SI | Date From |
| APCVM_DateTo | date |  |  | SI | Date To |
| APCVM_DiscDays | double |  |  | SI | Discount Days |
| APCVM_DiscRate | double |  |  | SI | Discount Rate |
| APCVM_Fax | varchar |  |  | SI | Fax No |
| APCVM_FwdBal | double |  |  | SI | Forward Month Balance |
| APCVM_Grading | varchar |  |  | SI | Grading |
| APCVM_LstInvDate | date |  |  | SI | Last Invoice Date |
| APCVM_LstPayDate | date |  |  | SI | Last Payment Date |
| APCVM_LstPoDate | date |  |  | SI | Last Purchase Date |
| APCVM_Name | varchar |  |  | SI | Vendor Name |
| APCVM_Owner | varchar |  |  | SI | Owner |
| APCVM_President | varchar |  |  | SI | President |
| APCVM_PrevBal | double |  |  | SI | Previous Month Balance |
| APCVM_RcFlag | varchar |  |  | SI | Archived Flag |
| APCVM_Registration | varchar |  |  | SI | Registration No |
| APCVM_ShName | varchar |  |  | SI | Vendor Short Name |
| APCVM_State_DR | bigint |  | FK | SI | Des Ref to CTSTT |
| APCVM_Status | varchar |  |  | SI | Status |
| APCVM_Tel | varchar |  |  | SI | Telephone No |
| APCVM_Type | varchar |  |  | SI | Vendor Type |
| APCVM_UpdatedDate | date |  |  | SI | Updated Date |
| APCVM_UpdatedTime | time |  |  | SI | Updated Time |
| APCVM_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| APCVM_Zip_DR | bigint |  | FK | SI | Des Ref to CTZIP |
| ChildQ54DR | - |  |  | SI | Child Reference: Antecedentes Último Examen |
| Q51Q1 | - |  |  | SI | Órgano/Tejido |
| Q51Q10 | - |  |  | SI | N° de Muestras |
| Q51Q2 | - |  |  | SI | Localización |
| Q51Q3 | - |  |  | SI | Lateralidad |
| Q51Q4 | - |  |  | SI | N° de Contenedores |
| Q51Q5 | - |  |  | SI | Diagnóstico Clínico |
| Q51Q6 | - |  |  | SI | Lateralidad |
| Q51Q7 | - |  |  | SI | ID Contenedor |
| Q51Q8 | - |  |  | SI | Tipo de Contenedor |
| Q51Q9 | - |  |  | SI | Precisión / Detalle |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*