# SQLUser.SS_UserDefWindowAgeSexRest

**Schema:** SQLUser
**Columnas:** 6
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Servicios de Sistema**. Configuración interna.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ASR_ParRef | bigint | PK |  | NO | SS_UserDefWindow Parent Reference |
| ASR_AgeFrom | varchar |  |  | SI | Age From |
| ASR_AgeTo | varchar |  |  | SI | AgeTo |
| ASR_Childsub | double |  |  | NO | Childsub |
| ASR_RowId | varchar |  |  | NO | - |
| ASR_Sex_DR | bigint |  | FK | SI | Des Ref Sex |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*