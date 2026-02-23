# SQLUser.OR_AnaestOrbitalAgent

**Schema:** SQLUser
**Columnas:** 4
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Pabellón Quirúrgico**. Gestión de cirugías.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ANOA_ParRef | varchar | PK |  | NO | OR_Anaesthesia Parent Reference |
| ANOA_ChildSub | numeric |  |  | NO | ChildSub |
| ANOA_RowId | varchar |  |  | NO | - |
| ANOA_Type_DR | bigint |  | FK | NO | Agent Des Ref to ORCAnaestAgent |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*