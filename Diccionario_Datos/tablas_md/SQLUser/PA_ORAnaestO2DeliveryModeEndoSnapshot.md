# SQLUser.PA_ORAnaestO2DeliveryModeEndoSnapshot

**Schema:** SQLUser
**Columnas:** 4
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PAEND_ParRef | bigint | PK |  | NO | PA_ORAnaestSnapshot Parent Reference |
| PAEND_ChildSub | double |  |  | NO | Childsub |
| PAEND_RowId | varchar |  |  | NO | - |
| PAEND_Type_DR | bigint |  | FK | SI | Des Ref ORCLineType |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*