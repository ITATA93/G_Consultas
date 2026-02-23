# SQLUser.PHC_AllergyGroupXSens

**Schema:** SQLUser
**Columnas:** 10
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Farmacia Clínica**. Validación farmacéutica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ALGRXS_ParRef | bigint | PK |  | NO | - |
| ALGRXS_AlGroup | bigint |  |  | SI | Des Ref Generic |
| ALGRXS_Childsub | double |  |  | NO | PHC_Generic Parent Reference
Childsub |
| ALGRXS_CreatedDate | date |  |  | SI | Created Date |
| ALGRXS_CreatedTime | time |  |  | SI | Created Time |
| ALGRXS_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ALGRXS_RowId | varchar |  |  | NO | - |
| ALGRXS_UpdatedDate | date |  |  | SI | Updated Date |
| ALGRXS_UpdatedTime | time |  |  | SI | Updated Time |
| ALGRXS_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*