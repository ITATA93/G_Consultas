# SQLUser.PA_ExtractDetails

**Schema:** SQLUser
**Columnas:** 10
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Detalle de la entidad padre.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DET_ParRef | bigint | PK |  | NO | PA_Extract Parent Reference |
| DET_Childsub | double |  |  | NO | Childsub |
| DET_PAADM_DR | bigint |  | FK | SI | Des Ref PAADM |
| DET_PAPMI_DR | bigint |  | FK | SI | Des Ref PAPMI |
| DET_RecordData | varchar |  |  | SI | RecordData |
| DET_RecordType | varchar |  |  | SI | RecordType |
| DET_RemoveDate | date |  |  | SI | RemoveDate |
| DET_RowId | varchar |  |  | NO | - |
| DET_Status | varchar |  |  | SI | Status |
| DET_WaitList_DR | bigint |  | FK | SI | Des Ref WaitList |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*