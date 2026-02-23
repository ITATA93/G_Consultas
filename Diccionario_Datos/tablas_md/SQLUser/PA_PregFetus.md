# SQLUser.PA_PregFetus

**Schema:** SQLUser
**Columnas:** 8
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| FET_ParRef | bigint | PK |  | NO | PA_Pregnancy Parent Reference |
| FET_Baby_DR | varchar |  | FK | SI | Reference to PAPregDel Baby |
| FET_Childsub | double |  |  | NO | Childsub |
| FET_Comments | varchar |  |  | SI | Free Text Description Field |
| FET_FetusID | varchar |  |  | SI | Manually entered Fetus ID |
| FET_FetusNumber | varchar |  |  | SI | Fetus Number |
| FET_IsExternalID | bit |  |  | SI | A Boolean for if the Fetus ID was external or inte... |
| FET_RowId | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*