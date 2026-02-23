# SQLUser.SS_GroupCodingStatus

**Schema:** SQLUser
**Columnas:** 4
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Estados posibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CODST_ParRef | bigint | PK |  | NO | SS_Group Parent Reference |
| CODST_Childsub | double |  |  | NO | Childsub |
| CODST_CodingStatus_DR | bigint |  | FK | SI | Des Ref CodingStatus |
| CODST_RowId | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*