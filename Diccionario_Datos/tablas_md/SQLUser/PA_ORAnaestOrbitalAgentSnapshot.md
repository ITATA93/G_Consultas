# SQLUser.PA_ORAnaestOrbitalAgentSnapshot

**Schema:** SQLUser
**Columnas:** 4
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PAAOA_ParRef | bigint | PK |  | NO | OR_Anaesthesia Parent Reference |
| PAAOA_ChildSub | numeric |  |  | NO | ChildSub |
| PAAOA_RowId | varchar |  |  | NO | - |
| PAAOA_Type_DR | bigint |  | FK | NO | Agent Des Ref to ORCAnaestAgent |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*