# SQLUser.PHC_ControlDrugCat

**Schema:** SQLUser
**Columnas:** 19
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Farmacia Clínica**. Validación farmacéutica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PHCCDC_RowId | bigint | PK |  | NO | - |
| PHCCDC_AllowReturnsFlag | varchar |  |  | NO | Allow Returns Flag |
| PHCCDC_CSDrugAdmFlag | varchar |  |  | NO | Counter Sign Drug Administration Flag |
| PHCCDC_CSOrderFlag | varchar |  |  | NO | Counter Sign Order Flag |
| PHCCDC_Code | varchar |  |  | NO | Controlled Drug Category Code |
| PHCCDC_CreatedDate | date |  |  | SI | Created Date |
| PHCCDC_CreatedTime | time |  |  | SI | Created Time |
| PHCCDC_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PHCCDC_Desc | varchar |  |  | NO | Description |
| PHCCDC_OEMsgFlag | varchar |  |  | NO | Display OE Message Flag |
| PHCCDC_PrescDetailsFlag | varchar |  |  | NO | Display Prescription Details Flag |
| PHCCDC_PrescFlag1 | varchar |  |  | NO | Prescription Flag: Generate Presc for Each Control... |
| PHCCDC_PrescFlag2 | varchar |  |  | NO | Prescription Flag: Generate Presc for Each Control... |
| PHCCDC_PrescValPeriod | double |  |  | SI | Prescription Validity Period |
| PHCCDC_RepeatsFlag | varchar |  |  | NO | Repeats Allowed Flag |
| PHCCDC_RestrPharmFlag | varchar |  |  | NO | Restricted Pharmacy Flag |
| PHCCDC_UpdatedDate | date |  |  | SI | Updated Date |
| PHCCDC_UpdatedTime | time |  |  | SI | Updated Time |
| PHCCDC_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*