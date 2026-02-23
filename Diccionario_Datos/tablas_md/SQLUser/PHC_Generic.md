# SQLUser.PHC_Generic

**Schema:** SQLUser
**Columnas:** 26
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Farmacia Clínica**. Validación farmacéutica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PHCGE_RowId | bigint | PK |  | NO | - |
| PHCGE_AllowAsAdMixAdditive | varchar |  |  | SI | Allow to order as Admixture Additive |
| PHCGE_AllowAsAdMixSolution | varchar |  |  | SI | Allow to order as Admixture Solution |
| PHCGE_AllowAsPCA | varchar |  |  | SI | Allow to order as PCA |
| PHCGE_AllowSubsNonBioequiv | varchar |  |  | SI | Allow to Substitute non-bioequivalent |
| PHCGE_BioequivWarning | varchar |  |  | SI | Bioequivalence Warning |
| PHCGE_Code | varchar |  |  | NO | Generic Code |
| PHCGE_ColourCode | varchar |  |  | SI | ColourCode  |
| PHCGE_ColourCodeText | varchar |  |  | SI | ColourCodeText  |
| PHCGE_CreatedDate | date |  |  | SI | Created Date |
| PHCGE_CreatedTime | time |  |  | SI | Created Time |
| PHCGE_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PHCGE_DateFrom | date |  |  | SI | Date From |
| PHCGE_DateTo | date |  |  | SI | Date To |
| PHCGE_DaysAfterMedsInterActive | double |  |  | SI | DaysAfterMedsInterActive |
| PHCGE_DosingGap | double |  |  | SI | Dosing Gap |
| PHCGE_LocalName | varchar |  |  | SI | LocalName  |
| PHCGE_MultiRoute | varchar |  |  | SI | This generic can be ordered as Multi-route |
| PHCGE_Name | varchar |  |  | NO | Generic Name |
| PHCGE_Owner | varchar |  |  | SI | Owner |
| PHCGE_PHCCL_DR | bigint |  | FK | SI | Des Ref to PHCCL |
| PHCGE_TimeCriticalWindow | varchar |  |  | SI | Time Critical Window (minutes) |
| PHCGE_Type | varchar |  |  | SI | Generic Type |
| PHCGE_UpdatedDate | date |  |  | SI | Updated Date |
| PHCGE_UpdatedTime | time |  |  | SI | Updated Time |
| PHCGE_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*