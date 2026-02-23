# SQLUser.SS_GroupMRRecordType

**Schema:** SQLUser
**Columnas:** 4
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| RT_ParRef | bigint | PK |  | NO | SS_Group Parent Reference |
| RT_Childsub | double |  |  | NO | Childsub |
| RT_MRRecordType_DR | bigint |  | FK | SI | Des Ref RTCMRecordType |
| RT_RowId | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*