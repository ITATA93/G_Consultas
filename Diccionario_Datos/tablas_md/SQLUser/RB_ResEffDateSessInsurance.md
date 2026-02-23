# SQLUser.RB_ResEffDateSessInsurance

**Schema:** SQLUser
**Columnas:** 5
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**RB Module**. Funcionalidad de módulos Rich Browser.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| INS_ParRef | varchar | PK |  | NO | RB_ResEffDateSession Parent Reference |
| INS_Childsub | double |  |  | NO | Childsub |
| INS_InsType_DR | bigint |  | FK | SI | Des Ref InsType |
| INS_NumberOfSlots | double |  |  | SI | Number Of Slots |
| INS_RowId | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*