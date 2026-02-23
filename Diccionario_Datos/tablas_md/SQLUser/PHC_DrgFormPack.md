# SQLUser.PHC_DrgFormPack

**Schema:** SQLUser
**Columnas:** 28
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Farmacia Clínica**. Validación farmacéutica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PACK_ParRef | varchar | PK |  | NO | PHC_DrgForm Parent Reference |
| PACK_AdvReaction | varchar |  |  | SI | Adverse Reaction (info) |
| PACK_Childsub | double |  |  | NO | Childsub |
| PACK_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| PACK_ContraInd | varchar |  |  | SI | Contra Indication (info) |
| PACK_CreatedDate | date |  |  | SI | Created Date |
| PACK_CreatedTime | time |  |  | SI | Created Time |
| PACK_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PACK_DateFrom | date |  |  | SI | DateFrom |
| PACK_DateTo | date |  |  | SI | DateTo |
| PACK_Description | varchar |  |  | SI | Description |
| PACK_Formulary | varchar |  |  | SI | Formulary |
| PACK_Indication | varchar |  |  | SI | Indication (info) |
| PACK_Interaction | varchar |  |  | SI | Interaction |
| PACK_MIMSno | varchar |  |  | SI | MIMS number |
| PACK_MaxNumberRepeats | double |  |  | SI | Max Number of Repeats |
| PACK_Monograph | varchar |  |  | SI | Monograph |
| PACK_PBSQuan | double |  |  | SI | PBS Quan |
| PACK_PHCPA_DR | bigint |  | FK | SI | Des Ref to PHCPA (Packing) |
| PACK_Poison_DR | bigint |  | FK | SI | Des Ref Poison |
| PACK_Precaution | varchar |  |  | SI | Special Precautions (info) |
| PACK_Preferred | varchar |  |  | SI | Preferred |
| PACK_Price1 | double |  |  | SI | Price 1 - MIMS (info) |
| PACK_RowId | varchar |  |  | NO | - |
| PACK_UpdatedDate | date |  |  | SI | Updated Date |
| PACK_UpdatedTime | time |  |  | SI | Updated Time |
| PACK_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| PACK_Warning | varchar |  |  | SI | Warning |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*