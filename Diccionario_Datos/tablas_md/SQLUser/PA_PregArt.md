# SQLUser.PA_PregArt

**Schema:** SQLUser
**Columnas:** 4
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PARM_ParRef | bigint | PK |  | NO | PA_Pregnancy Parent Reference |
| PARM_Childsub | double |  |  | NO | Childsub |
| PARM_Method_DR | bigint |  | FK | SI | Des Ref PAC_Art |
| PARM_RowId | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*