# SQLUser.OR_AnaestMonitorDevice

**Schema:** SQLUser
**Columnas:** 4
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Pabellón Quirúrgico**. Gestión de cirugías.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| MON_ParRef | varchar | PK |  | NO | OR_Anaesthesia Parent Reference |
| MON_Childsub | double |  |  | NO | Childsub |
| MON_Monit_DR | bigint |  | FK | SI | Des Ref Monitor |
| MON_RowId | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*