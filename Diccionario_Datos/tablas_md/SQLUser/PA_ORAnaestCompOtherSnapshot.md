# SQLUser.PA_ORAnaestCompOtherSnapshot

**Schema:** SQLUser
**Columnas:** 4
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PAACO_ChildSub | double | PK |  | NO | Childsub |
| PAACO_ParRef | bigint | PK |  | NO | PA_ORAnaestSnapshot Parent Reference |
| PAACO_RowId | varchar | PK |  | NO | - |
| PAACO_Type_DR | bigint | PK | FK | SI | Des Ref ORCAnaestComplications |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*