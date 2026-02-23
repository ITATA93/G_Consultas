# lab.CT_Personnel

**Schema:** lab
**Columnas:** 29
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTPER_RowId | varchar | PK |  | NO | - |
| CTPER_ActiveFlag | varchar |  |  | SI | Active Flag |
| CTPER_Address | varchar |  |  | SI | Address |
| CTPER_Address1 | varchar |  |  | SI | Address 1 |
| CTPER_Address2 | varchar |  |  | SI | Address 2 |
| CTPER_Address3_Suburb | varchar |  |  | SI | Suburb |
| CTPER_Address4_State_DR | varchar |  | FK | SI | State_DR |
| CTPER_Address5_PostCode | varchar |  |  | SI | Post Code |
| CTPER_ClientCode_DR | varchar |  | FK | SI | Client Code DR |
| CTPER_Code | varchar |  |  | NO | Code |
| CTPER_CollectionTimeEnd | varchar |  |  | SI | Collection Time End |
| CTPER_CollectionTimeSlot | varchar |  |  | SI | Collection Time Slot |
| CTPER_CollectionTimeStart | varchar |  |  | SI | Collection Time Start |
| CTPER_CollectorCode | varchar |  |  | SI | Collector Code |
| CTPER_Contact | varchar |  |  | SI | Contact |
| CTPER_DOB | date |  |  | SI | Date of Birth |
| CTPER_Department_DR | varchar |  | FK | SI | Department |
| CTPER_DisplaySequence | numeric |  |  | SI | Display Sequence |
| CTPER_EmployeeNumber | varchar |  |  | SI | Employee Number |
| CTPER_GName | varchar |  |  | SI | Given Name |
| CTPER_Phone | varchar |  |  | SI | Phone |
| CTPER_Position | varchar |  |  | SI | Position |
| CTPER_Salary | varchar |  |  | SI | Salary |
| CTPER_Sex_DR | varchar |  | FK | SI | Sex |
| CTPER_Super | varchar |  |  | SI | Super |
| CTPER_Surname | varchar |  |  | SI | Surname |
| CTPER_TaxFile | varchar |  |  | SI | Tax File |
| CTPER_Type_DR | varchar |  | FK | SI | Personnel Type |
| CTPER_UserSite_DR | varchar |  | FK | SI | User Site DR |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*