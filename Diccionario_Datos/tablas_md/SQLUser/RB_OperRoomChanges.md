# SQLUser.RB_OperRoomChanges

**Schema:** SQLUser
**Columnas:** 15
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**RB Module**. Funcionalidad de módulos Rich Browser.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CH_ParRef | bigint | PK |  | NO | RB_OperatingRoom Parent Reference |
| CH_Childsub | double |  |  | NO | Childsub |
| CH_Date | date |  |  | SI | Date |
| CH_LastUpdateHospital_DR | bigint |  | FK | SI | Des Ref LastUpdateHospital |
| CH_OperDepartment_DR | bigint |  | FK | SI | Des Ref OperDepartment |
| CH_Operation_DR | bigint |  | FK | SI | Des Ref Operation |
| CH_Priority_DR | bigint |  | FK | SI | Des Ref ORC Room Book Priority |
| CH_RB_Resource_DR | bigint |  | FK | SI | Des Ref Resource |
| CH_RowId | varchar |  |  | NO | - |
| CH_Sequence | varchar |  |  | SI | Sequence |
| CH_Status | varchar |  |  | SI | Status |
| CH_Surgeon_DR | varchar |  | FK | SI | Des Ref Surgeon |
| CH_Time | time |  |  | SI | Time |
| CH_TransDate | date |  |  | SI | Transaction Date |
| CH_TransTime | time |  |  | SI | Transaction Time |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*