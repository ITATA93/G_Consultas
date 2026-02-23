# SQLUser.SS_GroupDiagnosisType

**Schema:** SQLUser
**Columnas:** 5
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DTYPE_ParRef | bigint | PK |  | NO | SS_Group Parent Reference |
| DTYPE_Childsub | double |  |  | NO | Childsub |
| DTYPE_DefaultFlag | varchar |  |  | SI | Default Flag |
| DTYPE_DiagType_DR | bigint |  | FK | SI | Des Ref DiagType |
| DTYPE_RowId | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*