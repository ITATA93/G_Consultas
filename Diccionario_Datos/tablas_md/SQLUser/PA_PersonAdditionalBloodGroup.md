# SQLUser.PA_PersonAdditionalBloodGroup

**Schema:** SQLUser
**Columnas:** 8
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ABG_ParRef | bigint | PK |  | NO | PA_Person Parent Reference |
| ABG_AdditionalBloodGroup_DR | bigint |  | FK | SI | Des Ref Additional Blood Group |
| ABG_Childsub | double |  |  | NO | Childsub |
| ABG_RowID | varchar |  |  | NO | - |
| ABG_TestSetItem_DR | varchar |  | FK | SI | Test Set Item from which result is derived |
| ABG_UpdateDate | date |  |  | SI | Update Date |
| ABG_UpdateTime | time |  |  | SI | Update Time |
| ABG_UpdateUser_DR | bigint |  | FK | SI | Update User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*