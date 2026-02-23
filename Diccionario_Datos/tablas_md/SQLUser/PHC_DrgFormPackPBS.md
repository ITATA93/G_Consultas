# SQLUser.PHC_DrgFormPackPBS

**Schema:** SQLUser
**Columnas:** 11
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Farmacia Clínica**. Validación farmacéutica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PBS_ParRef | varchar | PK |  | NO | PHC_DrgFormPack Parent Reference |
| PBS_Childsub | double |  |  | NO | Childsub |
| PBS_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| PBS_CreatedDate | date |  |  | SI | Created Date |
| PBS_CreatedTime | time |  |  | SI | Created Time |
| PBS_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PBS_RowId | varchar |  |  | NO | - |
| PBS_StreamlineIndication_DR | bigint |  | FK | SI | Des Ref PHCStreamlineIndication |
| PBS_UpdatedDate | date |  |  | SI | Updated Date |
| PBS_UpdatedTime | time |  |  | SI | Updated Time |
| PBS_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*