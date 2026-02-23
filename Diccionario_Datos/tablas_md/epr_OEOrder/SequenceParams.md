# epr_OEOrder.SequenceParams

**Schema:** epr_OEOrder
**Columnas:** 9
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**EPR - Registro Electrónico de Pacientes**. Módulo de ficha clínica electrónica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ParRef | bigint | PK |  | NO | Par Ref |
| Childsub | numeric |  |  | NO | Childsub |
| ID | varchar |  |  | NO | - |
| OffsetExecDR | varchar |  | FK | SI | Offset Exec DR
Offset from this execution node |
| OffsetItemDR | bigint |  | FK | SI | Offset Item DR
Offset from this order item |
| OffsetType | varchar |  |  | SI | Offset Type
Standard Type OrderOffsetType  |
| OffsetUnit | varchar |  |  | SI | Offset Unit |
| OffsetValue | double |  |  | SI | Offset Value  |
| childsub1 | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*