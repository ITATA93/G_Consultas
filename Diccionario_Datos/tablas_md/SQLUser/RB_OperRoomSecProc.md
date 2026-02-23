# SQLUser.RB_OperRoomSecProc

**Schema:** SQLUser
**Columnas:** 10
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**RB Module**. Funcionalidad de módulos Rich Browser.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SPR_ParRef | bigint | PK |  | NO | RB_OperatingRoom Parent Reference |
| SPR_Childsub | double |  |  | NO | Childsub |
| SPR_DateOper | date |  |  | SI | Date of Operation |
| SPR_Laterality_DR | bigint |  | FK | SI | Des Ref Laterality |
| SPR_Operation_DR | bigint |  | FK | SI | Des Ref Operation |
| SPR_RowId | varchar |  |  | NO | - |
| SPR_StatePPP_DR | bigint |  | FK | SI | Des Ref StatePPP |
| SPR_SurgeonAssist_DR | varchar |  | FK | SI | Des Ref Surgeon Assistant |
| SPR_Surgeon_DR | varchar |  | FK | SI | Des Ref Surgeon |
| SPR_TimeOper | time |  |  | SI | Time of Operation |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*