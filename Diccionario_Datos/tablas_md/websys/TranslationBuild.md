# websys.TranslationBuild

**Schema:** websys
**Columnas:** 5
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Componente Web**. Interfaz de usuario del sistema TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| BuildDateTime | timestamp |  |  | NO | Build DateTime |
| Job | varchar |  |  | NO | Job that start the build |
| LanguageDR | bigint |  | FK | SI | Language DR |
| Running | bit |  |  | NO | State of running |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*