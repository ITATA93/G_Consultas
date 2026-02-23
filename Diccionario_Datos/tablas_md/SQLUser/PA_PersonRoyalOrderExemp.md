# SQLUser.PA_PersonRoyalOrderExemp

**Schema:** SQLUser
**Columnas:** 9
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| EXEMP_ParRef | varchar | PK |  | NO | PA_PersonRoyalOrder Parent Reference |
| EXEMP_ARCIM_DR | varchar |  | FK | SI | Des Ref ARCIM |
| EXEMP_BillGrp_DR | bigint |  | FK | SI | Des Ref BillGrp |
| EXEMP_BillSub_DR | varchar |  | FK | SI | Des Ref BillSub |
| EXEMP_Childsub | double |  |  | NO | Childsub |
| EXEMP_LimitAmount | double |  |  | SI | LimitAmount |
| EXEMP_RemainingAmount | double |  |  | SI | RemainingAmount |
| EXEMP_RowId | varchar |  |  | NO | - |
| EXEMP_UsedAmount | double |  |  | SI | UsedAmount |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*