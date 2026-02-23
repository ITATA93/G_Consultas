# SQLUser.PA_SLADetailsAllocatedMulti

**Schema:** SQLUser
**Columnas:** 4
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Detalle de la entidad padre.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| MULT_ParRef | bigint | PK |  | NO | PA_SLADetailsAllocated Parent Reference |
| MULT_Childsub | double |  |  | NO | Childsub |
| MULT_RowId | varchar |  |  | NO | - |
| MULT_ServAgreement_DR | bigint |  | FK | SI | Des REf ServAgreement |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*