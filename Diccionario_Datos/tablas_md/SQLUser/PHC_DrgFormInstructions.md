# SQLUser.PHC_DrgFormInstructions

**Schema:** SQLUser
**Columnas:** 13
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Farmacia Clínica**. Validación farmacéutica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| INSTRUCT_ParRef | varchar | PK |  | NO | PHC_DrgForm Parent Reference |
| INSTRUCT_Childsub | double |  |  | NO | Childsub |
| INSTRUCT_CreatedDate | date |  |  | SI | Created Date |
| INSTRUCT_CreatedTime | time |  |  | SI | Created Time |
| INSTRUCT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| INSTRUCT_DateFrom | date |  |  | SI | DateFrom |
| INSTRUCT_DateTo | date |  |  | SI | DateTo |
| INSTRUCT_PHCInstruc_DR | bigint |  | FK | SI | Des Ref to PHCInstruc |
| INSTRUCT_RowId | varchar |  |  | NO | - |
| INSTRUCT_Sequence | integer |  |  | SI | Sequence |
| INSTRUCT_UpdatedDate | date |  |  | SI | Updated Date |
| INSTRUCT_UpdatedTime | time |  |  | SI | Updated Time |
| INSTRUCT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*