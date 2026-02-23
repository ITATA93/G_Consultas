# SQLUser.PHC_DrgFormRepeatability

**Schema:** SQLUser
**Columnas:** 29
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Farmacia Clínica**. Validación farmacéutica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| REPEAT_ParRef | varchar | PK |  | NO | PHC_DrgForm Parent Reference |
| REPEAT_Childsub | double |  |  | NO | Childsub |
| REPEAT_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| REPEAT_CreatedDate | date |  |  | SI | Created Date |
| REPEAT_CreatedTime | time |  |  | SI | Created Time |
| REPEAT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| REPEAT_CurrentPrice | double |  |  | SI | Current price  |
| REPEAT_DateFrom | date |  |  | SI | Date From |
| REPEAT_DateTo | date |  |  | SI | Date To |
| REPEAT_DrugDispOnBehalf | varchar |  |  | SI | Drug dispensed on behalf    |
| REPEAT_DrugPrescClass | varchar |  |  | SI | Drug Prescription Class  |
| REPEAT_EVCategoryCode | varchar |  |  | SI | EV Category Code |
| REPEAT_HCA_DR | bigint |  | FK | SI | Des Ref HealthCareArea |
| REPEAT_HCR_DR | bigint |  | FK | SI | Des Ref HealthCareRegion |
| REPEAT_Licensable | varchar |  |  | SI | Licensable   |
| REPEAT_Nation | varchar |  |  | SI | Nation |
| REPEAT_NumberOfPacks | double |  |  | SI | Number of Packs |
| REPEAT_RepeatCategoryCode | varchar |  |  | SI | Repeat Category Code |
| REPEAT_Repeat_DR | bigint |  | FK | SI | Des Ref PHCRepeatability |
| REPEAT_RowId | varchar |  |  | NO | - |
| REPEAT_Text1 | varchar |  |  | SI | Text1 |
| REPEAT_Text2 | varchar |  |  | SI | Text2 |
| REPEAT_Text3 | varchar |  |  | SI | Text3 |
| REPEAT_UpdatedDate | date |  |  | SI | Updated Date |
| REPEAT_UpdatedTime | time |  |  | SI | Updated Time |
| REPEAT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| REPEAT_YesNo1 | varchar |  |  | SI | YesNo1 |
| REPEAT_YesNo2 | varchar |  |  | SI | YesNo2 |
| REPEAT_YesNo3 | varchar |  |  | SI | YesNo3 |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*