# SQLUser.OR_AnaestMethodType

**Schema:** SQLUser
**Columnas:** 4
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Pabellón Quirúrgico**. Gestión de cirugías. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ANATYPE_ParRef | varchar | PK |  | NO | MR_Adm Parent Reference |
| ANATYPE_Childsub | double |  |  | NO | Childsub |
| ANATYPE_RowId | varchar |  |  | NO | - |
| ANATYPE_Type_DR | bigint |  | FK | SI | Des Ref ORCVentilationMode |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*