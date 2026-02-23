# SQLUser.SS_GroupOrderStatusCat

**Schema:** SQLUser
**Columnas:** 8
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Estados posibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CAT_ParRef | varchar | PK |  | NO | SS_Group Parent Reference |
| CAT_AllowToDC | varchar |  |  | SI | Allow To D/C |
| CAT_AllowToDCPacked | varchar |  |  | SI | Allow To DC Packed |
| CAT_AllowToDCPaid | varchar |  |  | SI | Allow To DC Paid |
| CAT_Childsub | double |  |  | NO | Childsub |
| CAT_OrdCateg_DR | bigint |  | FK | SI | Des Ref OECOrderCategory |
| CAT_OrdSubCateg_DR | bigint |  | FK | SI | Des Ref ARCItemCat |
| CAT_RowId | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*