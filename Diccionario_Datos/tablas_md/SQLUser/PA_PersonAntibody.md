# SQLUser.PA_PersonAntibody

**Schema:** SQLUser
**Columnas:** 9
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ANTIB_ParRef | bigint | PK |  | NO | PA_Person Parent Reference |
| ANTIB_Active | varchar |  |  | SI | Active flag |
| ANTIB_Antibody_DR | bigint |  | FK | SI | Des Ref Antibody |
| ANTIB_Childsub | double |  |  | NO | Childsub |
| ANTIB_RowID | varchar |  |  | NO | - |
| ANTIB_TestSetItem_DR | varchar |  | FK | SI | Test Set Item from which result is derived |
| ANTIB_UpdateDate | date |  |  | SI | Update Date |
| ANTIB_UpdateTime | time |  |  | SI | Update Time |
| ANTIB_UpdateUser_DR | bigint |  | FK | SI | Update User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*