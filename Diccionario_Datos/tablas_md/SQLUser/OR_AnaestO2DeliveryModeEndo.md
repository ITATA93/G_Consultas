# SQLUser.OR_AnaestO2DeliveryModeEndo

**Schema:** SQLUser
**Columnas:** 4
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Pabellón Quirúrgico**. Gestión de cirugías.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ANAEND_ParRef | varchar | PK |  | NO | MR_Adm Parent Reference |
| ANAEND_Childsub | double |  |  | NO | Childsub |
| ANAEND_RowId | varchar |  |  | NO | - |
| ANAEND_Type_DR | bigint |  | FK | SI | Des Ref ORCLineType |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*