# SQLUser.SS_UserInsurance

**Schema:** SQLUser
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Servicios de Sistema**. Configuración interna.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| INS_ParRef | bigint | PK |  | NO | SS_User Parent Reference |
| INS_AuxInsType_DR | bigint |  | FK | SI | Des Ref AuxInsType |
| INS_CTLOC_DR | bigint |  | FK | SI | Des Ref CTLOC |
| INS_Childsub | double |  |  | NO | Childsub |
| INS_EpisodeType | varchar |  |  | SI | EpisodeType |
| INS_InsType_DR | bigint |  | FK | SI | Des Ref InsType |
| INS_RowId | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*