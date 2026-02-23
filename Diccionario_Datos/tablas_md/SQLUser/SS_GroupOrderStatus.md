# SQLUser.SS_GroupOrderStatus

**Schema:** SQLUser
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Estados posibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| OSTAT_ParRef | bigint | PK |  | NO | SS_Group Parent Reference |
| OSTAT_AllowToDC | varchar |  |  | SI | Allow To D/C |
| OSTAT_AllowToDCPacked | varchar |  |  | SI | Allow To DC Packed |
| OSTAT_AllowToDCPaid | varchar |  |  | SI | Allow To DC Paid |
| OSTAT_Childsub | double |  |  | NO | Childsub |
| OSTAT_OrdStat_DR | bigint |  | FK | SI | Des Ref OrdStat |
| OSTAT_RowId | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*