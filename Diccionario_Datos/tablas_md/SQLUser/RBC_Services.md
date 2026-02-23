# SQLUser.RBC_Services

**Schema:** SQLUser
**Columnas:** 31
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de RB**. Parámetros de módulos RB.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SER_RowId | bigint | PK |  | NO | - |
| SER_1stAppt | varchar |  |  | SI | 1st Appt |
| SER_ARCIM_DR | varchar |  | FK | SI | Des Ref ARCIM |
| SER_ARCOS_DR | varchar |  | FK | SI | Des Ref ARCOS |
| SER_Active | varchar |  |  | SI | Active |
| SER_AverageWeeksPYear | double |  |  | SI | AverageWeeksPYear |
| SER_CTCP_DR | varchar |  | FK | SI | Des Ref CTCP |
| SER_CTLOC_DR | bigint |  | FK | SI | Des Ref CTLOC |
| SER_CalcProjectedWait | varchar |  |  | SI | CalcProjectedWait |
| SER_CreatedDate | date |  |  | SI | Created Date |
| SER_CreatedTime | time |  |  | SI | Created Time |
| SER_CreatedUser_DR | bigint |  | FK | SI | Created User |
| SER_DateFrom | date |  |  | SI | Date From |
| SER_DateTo | date |  |  | SI | Date To |
| SER_Desc | varchar |  |  | SI | Description |
| SER_DescTranslated | varchar |  |  | SI | Description Translated (Computed) |
| SER_DressTime | double |  |  | SI | Dress Time (minutes) |
| SER_Equip_DR | bigint |  | FK | SI | Des Ref Equip |
| SER_ExtraContactPatientsPerc | double |  |  | SI | ExtraContactPatientsPerc |
| SER_FirstAvailable | varchar |  |  | SI | FirstAvailable |
| SER_Minutes | double |  |  | SI | Minutes |
| SER_NewWays | varchar |  |  | SI | NewWays |
| SER_NoOfSlots | double |  |  | NO | No Of Slots |
| SER_PFB | varchar |  |  | SI | PFB |
| SER_ProjectedWeeksWait | double |  |  | SI | ProjectedWeeksWait |
| SER_RowIdTranslated | varchar |  |  | SI | Code Translated (Computed) |
| SER_ServGroup_DR | bigint |  | FK | SI | Des Ref ServGroup |
| SER_SubCategoryDR | bigint |  | FK | SI | Sub Category Des ref |
| SER_UpdatedDate | date |  |  | SI | Updated Date |
| SER_UpdatedTime | time |  |  | SI | Updated Time |
| SER_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*