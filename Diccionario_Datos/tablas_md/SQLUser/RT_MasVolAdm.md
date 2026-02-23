# SQLUser.RT_MasVolAdm

**Schema:** SQLUser
**Columnas:** 5
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Tiempo Real**. Procesamiento en tiempo real.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ADM_ParRef | varchar | PK |  | NO | RT_MasVol Parent Reference |
| ADM_Childsub | double |  |  | NO | Childsub |
| ADM_PAADM_DR | bigint |  | FK | SI | Des Ref PAADM |
| ADM_RowId | varchar |  |  | NO | - |
| ADM_VolumeNotes | varchar |  |  | SI | Volume Notes |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*