# SQLUser.PA_PersonTooth

**Schema:** SQLUser
**Columnas:** 17
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| TOOTH_ParRef | bigint | PK |  | NO | PA_Person Parent Reference |
| TOOTH_Active | varchar |  |  | SI | Active |
| TOOTH_AllCurrentState_DR | varchar |  | FK | SI | Des Ref AllCurrentState_DR |
| TOOTH_Childsub | double |  |  | NO | Childsub |
| TOOTH_ColosCurrentState_DR | varchar |  | FK | SI | Des Ref ColosCurrentState |
| TOOTH_Comments | varchar |  |  | SI | Comments |
| TOOTH_Face1CurrentState_DR | varchar |  | FK | SI | Des Ref Face1CurrentState_DR |
| TOOTH_Face2CurrentState_DR | varchar |  | FK | SI | Des Ref Face2CurrentState_DR |
| TOOTH_Face3CurrentState_DR | varchar |  | FK | SI | Des Ref Face3CurrentState_DR |
| TOOTH_Face4CurrentState_DR | varchar |  | FK | SI | Des Ref Face4CurrentState_DR |
| TOOTH_Face5CurrentState_DR | varchar |  | FK | SI | Des Ref Face5CurrentState_DR |
| TOOTH_Number_DR | bigint |  | FK | SI | Des Ref Number_DR |
| TOOTH_Position_DR | bigint |  | FK | SI | Des Ref Position_DR |
| TOOTH_RootCurrentState_DR | varchar |  | FK | SI | Des Ref RootCurrentState_DR |
| TOOTH_RowId | varchar |  |  | NO | - |
| TOOTH_ToothCurrentState_DR | varchar |  | FK | SI | Des Ref ToothCurrentState_DR |
| TOOTH_Type_DR | bigint |  | FK | SI | Des Ref Type_DR |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*