# SQLUser.PA_ORAnaestVentModeSnapshot

**Schema:** SQLUser
**Columnas:** 4
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PAVENT_ParRef | bigint | PK |  | NO | PA_ORAnaestSnapshot Parent Reference |
| PAVENT_ChildSub | double |  |  | NO | Childsub |
| PAVENT_RowId | varchar |  |  | NO | - |
| PAVENT_Type_DR | bigint |  | FK | SI | Des Ref ORCVentilationMode |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*