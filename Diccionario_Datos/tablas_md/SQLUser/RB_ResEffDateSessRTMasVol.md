# SQLUser.RB_ResEffDateSessRTMasVol

**Schema:** SQLUser
**Columnas:** 9
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**RB Module**. Funcionalidad de módulos Rich Browser.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| RTMAV_ParRef | varchar | PK |  | NO | RB_ResEffDateSession Parent Reference |
| RTMAV_AllVolumes | varchar |  |  | SI | All Volumes |
| RTMAV_Childsub | double |  |  | NO | Childsub |
| RTMAV_LastTwoVolumes | varchar |  |  | SI | Last Two Volumes |
| RTMAV_LatestVolumeOnly | varchar |  |  | SI | Latest Volume Only |
| RTMAV_LeadTime | double |  |  | SI | Lead Time |
| RTMAV_RecordType_DR | bigint |  | FK | SI | Des Ref RecordType |
| RTMAV_RowId | varchar |  |  | NO | - |
| RTMAV_TypeVol_DR | varchar |  | FK | SI | Des Ref RTC_MRTypeVol_DR |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*