# SQLUser.PA_ORAnaestComplications

**Schema:** SQLUser
**Columnas:** 4
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PACOMP_ParRef | bigint | PK |  | NO | OR_Anaesthesia Parent Reference |
| PACOMP_ChildSub | double |  |  | NO | Childsub |
| PACOMP_Complic_DR | bigint |  | FK | SI | Des Ref ORCAnaComplic |
| PACOMP_RowId | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*